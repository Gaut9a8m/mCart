# mCart
Cool command line interface ready to use python api using docopt module.


Steps to follow:

1. zip extarct the code from github repo.
2. pip install docopt
3. type 'mcart.py -help' in cmd.
4. ready to use.


####### General usage informations #######

Usage:
 *   mcart.py init                                                               ---> initialize database.
 *   mcart.py admin add_prod <prod_name> <description> <amount> <category>       ---> add product to database by admin.
 *   mcart.py admin add_categories <cat_name>                                    ---> add category to database by admin.
 *   mcart.py admin view cart                                                    ---> Admin can view cart items.
 *   mcart.py admin view bill                                                    ---> Admin can bills genrated by user.
 *   mcart.py user add_to_cart <prod_name>                                       ---> USer can add item to cart.
 *   mcart.py user remove <prod_name>                                            ---> USer can remove item from cart.
 *   mcart.py user view_cat                                                      ---> USer can view different category.
 *   mcart.py user view_cart                                                     ---> USer can view cart items.
 *   mcart.py user view_prod [<category>]                                        ---> USer can view all products or product by category.
 *   mcart.py user checkout                                                      ---> USer can checkout and print bill of his purchase.
