import pandas as pd

daily_df = pd.read_csv("./data/daily_reports.csv")
"----------------------------------------------------------------"
totals_df = daily_df[["Confirmed", "Deaths", "Recovered"]
                     ].sum().reset_index(name="count")
totals_df = totals_df.rename(columns={"index": "condition"})
"----------------------------------------------------------------"
countries_df = daily_df[["Country_Region", "Confirmed", "Deaths", "Recovered"]]
countries_df = countries_df.groupby("Country_Region").sum().reset_index()

"================================================================"
conditions = ["confirmed", "deaths", "recovered"]
global_df = None
country_df = None


def make_global_df():
    conditions = ["confirmed", "deaths", "recovered"]
    final_df = None

    def make_df(condition):
        df = pd.read_csv(f"data/time_{condition}.csv")
        df = df.drop(["Province/State", "Country/Region",
                      "Lat", "Long"], axis=1).sum()
        df = df.reset_index(name=condition).rename(columns={"index": "date"})
        return df
    for condition in conditions:
        df = make_df(condition)
        if final_df is None:
            final_df = df
        else:
            final_df = pd.merge(final_df, df)
    return final_df


def make_country_df(country):
    conditions = ["confirmed", "deaths", "recovered"]
    final_df = None

    def make_df(condition):
        time_df = pd.read_csv(f"data/time_{condition}.csv")
        booleans = time_df["Country/Region"] == country
        df = time_df.loc[booleans]
        df = df.drop(["Province/State", "Country/Region", "Lat",
                     "Long"], axis=1).sum().reset_index(name=condition)
        df = df.rename(columns={"index": "date"})
        return df

    for condition in conditions:
        df = make_df(condition)

        if final_df is None:
            final_df = df
        else:
            final_df = final_df.merge(df)
    return final_df
