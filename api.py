import sqlite3 as db
from datetime import datetime

conn = db.connect("mycart.db")
cur = conn.cursor()


def init():
    
    sql1='''
        create table if not exists product(
          amount number,
          category string,
          product_name string,
          description string,
          date string
        )
    '''
    sql2='''
        create table if not exists category(
          category_name string,
          date string
        )
    '''
    sql3='''
        create table if not exists cart(
          product_name string,
          amount number,
          quantity number,
          date string
        )
    '''
    
    cur.execute(sql1)
    cur.execute(sql2)
    cur.execute(sql3)
    conn.commit()
    print("database created successfully")

def add_prod(prod_name,description,amount,category):          #function to add new product to database by admin
    date = str(datetime.now())
    mssg = ""
    try:
        sql='''
        select * from category where category_name = '{}'
        '''.format(category)
        cur.execute(sql)
        result = cur.fetchone()
        if not result:
            add_cat(category)

        sql='''
        insert into product values('{}','{}','{}','{}','{}')
        '''.format(amount,category,prod_name,description,date)
        cur.execute(sql)
        conn.commit()
        mssg = "success fully added"
        
            
    except OSError as err:
        mssg = "something went wrong: {}".format(err)
    return {'status':mssg}


# add_prod("pencil box","a pencil box",120, "stationary")


def add_cat(category_name):          #function to add new category to database by admin
    date = str(datetime.now())
    mssg = ""
    try:
        sql='''
        insert into category values('{}','{}')
        '''.format(category_name,date)
        cur.execute(sql)
        conn.commit()
        mssg = "success fully added"
    except OSError as err:
        mssg = "something went wrong: {}".formart(err)
    return {'status':mssg}



def cart(product_name):          #function to add product to cart for checkout by user
    date = str(datetime.now())
    mssg = ""
    amount = 0
    try:
        sql='''
        select product_name,amount from product where product_name= '{}'
        '''.format(product_name)
        cur.execute(sql)
        result = cur.fetchall()
        # print('here is list of item: {}'.format(result[0][0]))
        amount = int(result[0][1])

        sql='''
        select product_name,quantity from cart where product_name = '{}'
        '''.format(product_name)
        cur.execute(sql)
        qty = cur.fetchall()
        
        if not qty:
            sql='''
            insert into cart values('{}','{}','{}','{}')
            '''.format(product_name,amount,1,date)
            cur.execute(sql)
            conn.commit()
        else:
            # print(qty[0][1])
            sql='''
            update cart set quantity = '{}' where product_name = '{}'
            '''.format(int(qty[0][1])+1,product_name)
            cur.execute(sql)
            conn.commit()
        mssg = "success fully added"
    except OSError as err:
        mssg = "something went wrong: {}".formart(err)
    return {'status':mssg}

# cart("box")

def remove_cart(product_name):          #function to remove product from cart by user
    mssg = ""
    try:
        sql='''
        select product_name,quantity from cart where product_name = '{}'
        '''.format(product_name)
        cur.execute(sql)
        result = cur.fetchall()
        # print(result)
        if result:
            if result[0][1]<=1:
                sql='''
                delete from cart where product_name = '{}'
                '''.format(product_name)
                cur.execute(sql)
                conn.commit()
                mssg = "success"
            elif result[0][1]>1:
                sql='''
                update cart set quantity = '{}' where product_name = '{}'
                '''.format(result[0][1]-1,product_name)
                cur.execute(sql)
                conn.commit()
                mssg = "success"
        else:
            mssg = "no product found with the given name"
            return {'status':mssg}
    except OSError as err:
        mssg = "something went wrong: {}".formart(err)
    return {'status':mssg, 'result': view_cart()}


# remove_cart("box")

def checkout():     # final checkout function to calculate the amount and discount on prouct purchased by user.
    date = str(datetime.now())
    discount = 0
    final_amount = 0
    actual_amount = 0
    mssg = "Thanks for visiting...."
    sql='''
    select * from cart
    '''
    cur.execute(sql)
    cart_value = cur.fetchall()
 
    for item in cart_value:
        # print(item)
        actual_amount += item[1]*item[2]
        
    if actual_amount > 10000 :
        discount = 500
        final_amount = actual_amount - discount
    else:
        final_amount = actual_amount
    cart_value.append({'final_amount':final_amount,'actual_amount':actual_amount,'discount':discount})
    return {'status':mssg,'result':cart_value}


# checkout()

def view_cart():          #function to view cart items by user as well as by admin
    sql='''
    select * from cart
    '''
    cur.execute(sql)
    result = cur.fetchall()
    return result

# view_cart()


def view_category():          #function to all view_category by user
    
    sql='''
    select * from category
    '''
    cur.execute(sql)
    result = cur.fetchall()
    return result

# view_cart()

def view_prod(category=None):          #function to product by category or all product by user
    if not category:
        sql='''
        select * from product
        '''
    else:
        sql='''
        select * from product where category = '{}'
        '''.format(category)
    cur.execute(sql)
    result = cur.fetchall()
    return result

# view_cart()


# if __name__ == "__main__":
    # init()
    # print(add_cat("stationary"))
    # print(add_cat("grocery"))
    # print(add_cat("electronic"))
    # print(add_cat("fashion"))
    # print(view_category())
    # print(add_prod("pencil box","a pencil box",120, "stationary"))
    # print(add_prod("tube light","a tube light 25Watt",300, "electronic"))
    # print(add_prod("mustard oil","250ml mustard oil bottle",110, "grocery"))
    # print(add_prod("T-shirt unisex","a white T-shirt size-M unisex",499, "fashion"))
    # print(add_prod("T-shirt mens","a black T-shirt size-M mens",499, "fashion"))
    # print(add_prod("sofa","a pylwood 4 seater sofa",1499, "wooden"))
    # print(view_prod())
    # print(view_prod("fashion"))
    # print(view_category())

    # print(cart("tube light"))
    # print(cart("pencil box"))
    
    # print(checkout())
    # print(remove_cart("pencil box"))
   