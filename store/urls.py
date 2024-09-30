from django.urls import path
from .views import Home,Signup,Login,logout,Cart,Checkout,OrderView,admincnt
from .views.suppliersignup import SupplierSignupView
from .views.supplierlogin import SupplierLoginView, logouts
	
from .views.supplierproduct import SupplierDashView
from .views.supreqview import view_messages , process_request , complete_request, delete_request, reject_request, delete_rejected_requests
from .middlewares import LoginCheckMiddleware,LogoutCheckMiddleware
from .views import supplyreq
from . import views
from .views.supplybill import view_bill
from .views.admincnt import *
from .views.allpage import AllPageView
from store.views.search import search_view
from store.views.profile import ProfileView
from store.views.editprofile import EditProfileView
from store.views.ChangePassword import ChangePasswordView
from store.views.ForgetPassword import ForgetPasswordView
from store.views.admincnt import send_bill, get_supplier_product_pdf,InStockPageView
from store.views.order import cancel_order
from store.views.suDash import suDash
from store.views.suplistview import viewprdlist
from store.views.game_optimizer import GameOptimizerView
from store.views.recomention import game_recommendation_view
from store.views.bot import *
from django.views.generic import TemplateView
urlpatterns = [
    path('home/',Home.as_view(), name='home'),
    path('', AllPageView.as_view(), name='allpage'),
    path('signup',LogoutCheckMiddleware(Signup.as_view()), name='signup'),
    path('login/',LogoutCheckMiddleware(Login.as_view()), name='login'),
    path('logout',LoginCheckMiddleware(logout), name='logout'),
    path('cart',Cart.as_view(), name='cart'),
    path('checkout',LoginCheckMiddleware(Checkout.as_view()), name='checkout'),
    path('viewBill',LoginCheckMiddleware(admincnt.viewBill), name='viewBill'),
    path('order',LoginCheckMiddleware(OrderView.as_view()), name='order'),
    path('order/<int:order_id>/pdf/', OrderView.as_view(), name='order-pdf'),
    path('cancel-order/<int:order_id>/', cancel_order, name='cancel-order'),
    path('search/', search_view, name='search'),
    path('profile/',LoginCheckMiddleware( ProfileView.as_view()), name='profile'),
    path('edprofile/',LoginCheckMiddleware( EditProfileView.as_view()), name='edprofile'),
    path('change_password/', LoginCheckMiddleware(ChangePasswordView.as_view()), name='change_password'),
    path('game_optimizer/', GameOptimizerView.as_view(), name='game_optimizer'),
    
    path('recommendations/', game_recommendation_view, name='game_recommendations'),
# Add this line in your urls.py
    path('forget_password/', LogoutCheckMiddleware(ForgetPasswordView.as_view()), name='forget_password'),

    path('logout/', LoginCheckMiddleware(logout), name='supplier_logout'),
    path('suppliersignup/', LogoutCheckMiddleware(SupplierSignupView.as_view()), name='suppliersignup'),
    path('supplier/', LogoutCheckMiddleware(SupplierLoginView.as_view()), name='supplierlogin'),
    path('supplier/dashboard/', SupplierDashView.as_view(), name='supplier_dashboard'),
    path('in_stock/', InStockPageView.as_view(), name='in_stock_page'),
    path('su-dashboard/', suDash, name='su_dashboard'),
    
    path('submit_supply_request/', supplyreq.submit_supply_request, name='submit_supply_request'),
    path('view-messages/', view_messages, name='view_messages'), 
    path('supplier/requests/', supplyreq.supplier_requests, name='supplier_requests'),  # New supplier view path
    path('process-request/<int:request_id>/', process_request, name='process_request'),  # New URL pattern
    path('view-messages/', view_messages, name='view_supply_requests'),  # Corrected the function name
    path('complete/<int:request_id>/', complete_request, name='complete_request'),
    path('reject/<int:request_id>/', reject_request, name='reject_request'),
    path('delete/<int:request_id>/', delete_request, name='delete_request'),
    path('delete_supply_request/<int:request_id>/', supplyreq.delete_supply_request, name='delete_supply_request'),
    path('supply-requests/delete-rejected/', delete_rejected_requests, name='delete_rejected_requests'),  # Import and include the delete_supply_request URL pattern
    path('view_bill/<int:product_id>/', view_bill, name='view_bill'),
    path('send_bill/', send_bill, name='send_bill'),
    path('deleteproduct/<int:product_id>/', admincnt.delete_product, name='delete_product'),
    path('supplier_product_pdf/<int:product_id>/', get_supplier_product_pdf, name='supplier_product_pdf'),
    path('viewprdlist/', viewprdlist, name='viewprdlist'),
    path('visualizations/', visualizations, name='visualizations'),


    
    path('admins/', admincnt.index, name='index'),
    path('admins/addcat', admincnt.addcats, name='addcats'),
    path('admins/adlogin', admincnt.adminlogin, name='adlogin'),
    path('admins/viewcat', admincnt.viewcat, name='viewcat'),
    path('admins/editcat', admincnt.editcats, name='editcat'),
    path('admins/addproduct', admincnt.addproduct, name='addproduct'),
    path('admins/viewprd', admincnt.viewprd, name='viewproduct'),
    path('admins/viewporder', admincnt.viewporder, name='viewporder'),
    path('admins/logouts', admincnt.logouts, name='logouts'),
    path('admins/editproduct', admincnt.editproduct, name='editproduct'),
    path('admins/game-sales-report', game_sales_report, name='game_sales_report'),
       # Renders the main chat page
    path('chatbot/', chatbot_view, name='chatbot'),  # Chatbot page
    
    
    
    
]


