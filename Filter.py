import pandas as pd
import psycopg2



def stuck(mes):
    pair = ''
    # Basic Parameters...
    PGHOST = "localhost"
    PGDATABASE = "dbname"
    PGUSER = "user"
    PGPASSWORD = "pswrd"

    # Connect The Database...
    postgresConnection = psycopg2.connect(database=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST)

    # Connection In Autocommit...
    postgresConnection.autocommit = True

    # Set Cursor Point....
    cursor = postgresConnection.cursor()
    import re
    # f_set = ''
    message = str(mes.text)
    try:
        message = message.lower()

        def data_var(take_p, t_p):
            list1 = [take_p, t_p]
            final = ''
            for i in list1:
                try:
                    attr_search = re.search(r"\b" + re.escape(i) + r"\b", message).span()
                    attr_search = attr_search[-1]
                    dr = re.search('[0-9.,]+', message[attr_search:])
                    try:
                        dr = dr.group()
                    except Exception:
                        pass
                    final = final+ dr


                except Exception:
                    pass
            return final

        import pandas as pd
        srp = pd.read_csv(r"C:\Users\DELL\PycharmProjects\Exam\Forex\Book1.csv")
        level = len(srp)
        for i in range(level):
            stock = str(srp['stock'].iloc[i])
            pair_name = stock.lower()
            try:
                attr_search = re.search(r"\b" + re.escape(pair_name) + r"\b", message).span()
                attr_search = attr_search[-1]
                dr = re.search('[0-9.,]+', message[attr_search:])
                dr = dr.group()
                pair = pair + pair_name

                if len(str(dr)) > 1:
                    cursor.execute("UPDATE stock_data SET pair = '"+ pair_name +"'")
                    cursor.execute("UPDATE stock_data SET price = "+ dr +" WHERE pair = '" +pair_name + "'")
                # f_set = f_set + "\n" + final
            except Exception:
                try:
                    cursor.execute("UPDATE stock_data SET "+ dr +" = Null")
                except Exception:
                    pass
                    # print(e)
                pass



        for i in range(8):
            t1 = "take profit"
            t2 = "tp"
            take_p = t1 + " " + str(i)
            t_p = t2 + str(i)

            if i == 0:
                try:
                    tp_0 = data_var(t1, t2)
                    # f_set = f_set + "\n" + final
                    cursor.execute("UPDATE stock_data SET "+ t2 +" = " + tp_0 + " WHERE pair = '" + pair + "'")
                except Exception:
                    try:
                        cursor.execute("UPDATE stock_data SET "+ t2 +" = Null")
                    except Exception as e:
                        print(e)
                        pass
                    pass
            elif i == 1:
                try:
                    tp_1 = data_var(take_p, t_p)
                    # f_set = f_set + "\n" + final
                    cursor.execute("UPDATE stock_data SET "+ t_p +" = " + tp_1 + " WHERE pair = '" + pair + "'")


                except Exception:
                    try:
                        cursor.execute("UPDATE stock_data SET "+ t_p +" = Null")
                    except Exception as e:
                        print(e)
                        pass
                    # print(e)
                    pass
            else:
                try:
                    tp_all = data_var(take_p, t_p)
                    # f_set = f_set + "\n" + final
                    cursor.execute("UPDATE stock_data SET "+ t_p +" = " + tp_all + " WHERE pair = '" + pair + "'")
                except Exception:
                    # print(e)
                    try:
                        cursor.execute("UPDATE stock_data SET "+ t_p +" = Null")
                    except Exception:
                        pass
                    pass

        try:
            if "sl" or "stop loss" in message:
                sl_price = data_var("stop loss", "sl")
                # f_set = f_set + "\n" + final
                cursor.execute("UPDATE stock_data SET sl = " + sl_price + " WHERE pair = '" + pair + "'")
        except Exception:
                # print(e)
                try:
                    cursor.execute("UPDATE stock_data SET sl = Null")
                except Exception:
                    pass
                pass
        try:
            if "be" or "break even" in message:
                be_price = data_var("break even", "be")
                # f_set = f_set + "\n" + final
                cursor.execute("UPDATE stock_data SET be = " + be_price + " WHERE pair = '" + pair + "'")
        except Exception:
            # print(e)
            try:
                cursor.execute("UPDATE stock_data SET be = Null")
            except Exception:
                pass

            pass
        try:
            if "cmp" or "current market price" in message:
                cmp_price = data_var("current market price", "cmp")
                # f_set = f_set + "\n" + final
                cursor.execute("UPDATE stock_data SET cmp = " + cmp_price + " WHERE pair = '" + pair + "'")
        except Exception:
            # print(e)
            try:
                cursor.execute("UPDATE stock_data SET cmp = Null")
            except Exception:
                pass
            pass
        try:
            if "sellstop" or "sell stop" in message:
                ss_final = data_var("sellstop", "sell stop")
                # print(final)
                # f_set = f_set + "\n" + final
                cursor.execute("UPDATE stock_data SET sellstop = " + ss_final + " WHERE pair = '" + pair + "'")
        except Exception:
            # print(e)
            try:
                cursor.execute("UPDATE stock_data SET sellstop = Null")
            except Exception:
                pass
            pass

        try:
            if "selllimit" or "sell limit" in message:
                sl_final = data_var("selllimit", "sell limit")
                # print(final)
                # f_set = f_set + "\n" + final
                cursor.execute("UPDATE stock_data SET selllimit = " + sl_final + " WHERE pair = '" + pair + "'")


        except Exception:

            # print(e)
            try:
                cursor.execute("UPDATE stock_data SET selllimit = Null")
            except Exception:
                pass
            pass

        try:
            if "buystop" or "buy stop" in message:
                bs_final = data_var("buystop", "buy stop")
                # print(final)
                # f_set = f_set + "\n" + final
                cursor.execute("UPDATE stock_data SET buystop = " + bs_final + " WHERE pair = '" + pair + "'")


        except Exception:

            # print(e)
            try:
                cursor.execute("UPDATE stock_data SET buystop = Null")
            except Exception:
                pass
            pass

        try:
            if "buylimit" or "buy limit" in message:
                bl_final = data_var("buylimit", "buy limit")
                # print(final)
                # f_set = f_set + "\n" + final
                cursor.execute("UPDATE stock_data SET buylimit = " + bl_final + " WHERE pair = '" + pair + "'")


        except Exception:

            # print(e)
            try:
                cursor.execute("UPDATE stock_data SET buylimit = Null")
            except Exception:
                pass
            pass


        try:
            if "buy" in message:
                buy_final = data_var("buy", "ABC")
                # print(final)
                # f_set = f_set + "\n" + final
                cursor.execute("UPDATE stock_data SET buy = " + buy_final + " WHERE pair = '" + pair + "'")


        except Exception:

            # print(e)
            try:
                cursor.execute("UPDATE stock_data SET buy = Null")
            except Exception:
                pass
            pass


        try:
            if "sell" in message:
                sell_final = data_var("sell", "ABC")
                # print(final)
                # f_set = f_set + "\n" + final
                cursor.execute("UPDATE stock_data SET sell = " + sell_final + " WHERE pair = '" + pair + "'")


        except Exception:

            # print(e)
            try:
                cursor.execute("UPDATE stock_data SET sell = Null")
            except Exception:
                pass
            pass
    except Exception:
        pass

    return pair,cursor