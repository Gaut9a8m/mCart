usage = '''
**************************** M-Cart an e-Commerce CLI application **************************** 

Usage:
    mcart.py init
    mcart.py admin add_prod <prod_name> <description> <amount> <category>
    mcart.py admin add_categories <cat_name>
    mcart.py admin view cart
    mcart.py admin view bill
    mcart.py user add_to_cart <prod_name>
    mcart.py user remove <prod_name>
    mcart.py user view_cat
    mcart.py user view_cart
    mcart.py user view_prod [<category>]
    mcart.py user checkout

'''

from docopt import docopt
from api import *
args = docopt(usage)
# print(args)
if args['init']:
    init()
elif args['admin']:
    if args['add_categories']:
        print(add_cat(args['<cat_name>']))
    elif args['add_prod']:
        print(add_prod(args['<prod_name>'],args['<description>'],int(args['<amount>']),args['<category>']))
    elif args['view']:
        if args['cart']:
            print(view_cart())
        elif args['bill']:
            print(view_bill())
        else:
            print("syntax invalid!!!")
            print("Please check documentation")
            print(args)
elif args['user']:
    if args['add_to_cart']:
        print(cart(args['<prod_name>'])) 
    elif args['remove'] :
        print(remove_cart(args['<prod_name>']))
    elif args['view_cat']:
        print(view_category())
    elif args['view_cart']:
        print(view_cart())
    elif args['view_prod']:
        print(view_prod(args['<category>']))
    elif args['checkout']:
        print(checkout())
    else:
        print("syntax invalid!!!")
        print("Please check documentation")
        print(args)
else:
    print("syntax invalid!!!")
    print("Please check documentation")
    print(args)