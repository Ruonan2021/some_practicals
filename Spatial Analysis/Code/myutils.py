
# count distinct value of a column, default by ascending
def group_by_count(df, col_name, asc = False):
    return df.groupby([col_name]).size().sort_values(ascending=asc)

def group_by_count2(df, col_name1, col_name2, asc = False):
    print("hhhhh")
    return df.groupby([col_name1, col_name2]).size().sort_values(ascending=asc)

def test():
    return "here we are"

def test2():
    return "here we are"