# package: container of multiple modules

# __init__.py 

# 1
# import ecommerce.shipping
#
# ecommerce.shipping.calc_shipping()
# ecommerce.shipping.calc_tax()

# 2
# from ecommerce.shipping import calc_shipping, calc_tax
#
# calc_shipping()
# calc_tax()

# 3
from ecommerce import shipping
shipping.calc_shipping()
shipping.calc_tax()

