# group by one column, col_name is a str
def group_by_percentage(df, col_name, asc = False):
    series_count = df.groupby([col_name]).size().sort_values(ascending=asc)
    df_count = series_count.to_frame(name = 'count').reset_index()
    df_count['percentage'] = round((df_count['count'] / df_count['count'].sum()) * 100, 2)
    return df_count

 # Group by multiple columns, cols is a list of str, groupBy1 is a str(need improve)
def group_by_percentage_cols(df, cols, groupBy1):
    df_out = df_merge.groupby(cols).size().to_frame("count").reset_index()
    df_out["pct"] = df_out["count"] / df_out.groupby(groupBy1)["count"].transform("sum")
    df_out["pct"] = df_out["pct"].multiply(100).round(2)
    return df_out

def compare_two_df(df1, df2, col_name):
    df1_percent = group_by_percentage(df1, col_name)
    df2_percent = group_by_percentage(df2, col_name)

    return df1_percent.merge(df2_percent, on = col_name)
