import gql from "graphql-tag";
import { createRouter, createWebHistory } from "vue-router";
import { ApolloClient, createHttpLink, InMemoryCache } from '@apollo/client/core'

import store from '../store'

import Home from '../views/Home.vue'

import Product from '../views/Product.vue'
import Category from '../views/Category.vue'
import Search from '../views/Search.vue'
import Cart from '../views/Cart.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'
import Checkout from '../views/Checkout.vue'
import Success from '../views/Success.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { requiresAuth: false }
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue'),
    meta: { requiresAuth: false }
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp,
    meta: { requiresAuth: false }
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn,
    meta: { requiresAuth: false }
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/search',
    name: 'Search',
    component: Search,
    meta: { requiresAuth: false }
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart,
    meta: { requiresAuth: false }
  },
  {
    path: '/cart/success',
    name: 'Success',
    component: Success,
    meta: { requiresAuth: false }
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: Checkout,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/:category_slug/:product_slug',
    name: 'Product',
    component: Product,
    meta: { requiresAuth: false }
  },
  {
    path: '/:category_slug',
    name: 'Category',
    component: Category,
    meta: { requiresAuth: false }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const apolloClient = new ApolloClient({
  link: createHttpLink({ uri: 'http://localhost:4000/' }),
  cache: new InMemoryCache()
})

async function isAuth() {
  if (localStorage.getItem("token_access") === null || localStorage.getItem("token_refresh") === null) {
      return false;
  }

  try {
      var result = await apolloClient.mutate({
          mutation: gql `
              mutation ($refresh: String!) {
                  refreshToken(refresh: $refresh) {
                      access
                  }
              }
          `,
          variables: {
              refresh: localStorage.getItem("token_refresh"),
          },
      })

      localStorage.setItem("token_access", result.data.refreshToken.access);
      return true;
  } catch {
      localStorage.clear();
      alert("Su sesión expiró, por favor vuelva a iniciar sesión");
      return false;
  }
}

router.beforeEach(async(to, from) => {
  var is_auth = await isAuth();

  if (is_auth == to.meta.requiresAuth) return true
  if (is_auth) return { name: "MyAccount" };
  return { name: "LogIn" };
})

export default router;





