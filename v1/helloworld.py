


def vehicle_clean(df, spark):
    """
    """

    df.registerTempTable('df')
    sql = """
    SELECT *,
     CASE WHEN Vehicle IS NULL THEN 'Not known'
         ELSE Vehicle
     END as der_name
    from df
    """

    df = spark.sql(sql)
    return df   





def add(a,b):
    c = a + b
    return c



