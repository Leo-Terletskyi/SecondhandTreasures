import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CategoryPage from "@/views/CategoryPage";
import ProductPage from "@/views/ProductPage";
import SearchVue from "@/views/SearchVue";
import CartVue from "@/views/CartVue";

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    },
    {
        path: '/search',
        name: 'search',
        component: SearchVue
    },
    {
        path: '/cart',
        name: 'cart',
        component: CartVue
    },
    {
        path: '/:category_slug',
        name: 'categoryPage',
        component: CategoryPage
    },
    {
        path: '/:category_slug/:product_slug',
        name: 'productPage',
        component: ProductPage
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
