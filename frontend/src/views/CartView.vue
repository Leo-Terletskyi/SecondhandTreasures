<template>
  <div class="page-cart">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">
          Cart
        </h1>
      </div>
      <div class="column is-12 box has-background-grey-light">
        <table class="table is-fullwidth has-background-dark" v-if="cartTotalLength">
          <thead>
          <tr>
            <th class="has-text-white">Product</th>
            <th class="has-text-white">Price</th>
            <th class="has-text-white">Quantity</th>
            <th class="has-text-white">Total</th>
            <th></th>
          </tr>
          </thead>
          <tbody>
          <CartItem
              v-for="item in cart.items"
              :key="item.product.id"
              :initialItem="item"
              v-on:removeFromCart="removeFromCart"
          />
          </tbody>
        </table>
        <p v-else>
          You don't have any products in your cart...
        </p>
      </div>
      <div class="column is-12 box">
        <h2 class="subtitle">
          Summary
        </h2>
        <strong>
          <span class="has-text-primary">
            $
          </span>
          {{ cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} items
        <hr>
        <router-link to="/cart/checkout" class="button is-dark">
          Proceed to checkout
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {toast} from 'bulma-toast';

import CartItem from "@/components/CartItem";

export default {
  name: 'CartView',
  components: {CartItem},
  data() {
    return {
      cart: {
        items: []
      },
      productsList: [],
      checkedProducts: [],
    }
  },
  async mounted() {
    this.cart = this.$store.state.cart
    await this.getProductsForCheck()
    await this.getProductsList()
    await this.confirmCheckProducts()
  },
  computed: {
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => {
        return acc += curVal.quantity
      }, 0)
    },
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return acc += curVal.product.price * curVal.quantity
      }, 0)
    },
  },
  methods: {
    removeFromCart(item) {
      this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
    },
    getProductsForCheck() {
      const rawObject = JSON.parse(JSON.stringify(this.cart.items))
      for (let item of rawObject) {
        this.productsList.push(item.product.slug)
      }
    },
    confirmCheckProducts() {
      if (this.cart.items.length === 0) {
        return
      }
      this.checkedProducts.forEach((i) => {
        let copyOfCart = this.cart.items.slice()
        for (let tmp = 0; tmp < copyOfCart.length; tmp++) {
          if (i.id === copyOfCart[tmp].product.id) {
            if (i.quantity <= 0) {
              this.removeFromCart(copyOfCart[tmp])
              localStorage.setItem('cart', JSON.stringify(this.cart))
              toast({
                message: `Sorry, but product ${copyOfCart[tmp].product.name} is out of stock`,
                type: "is-warning",
                position: "center",
                duration: 8000,
                pauseOnHover: true,
                dismissible: true,
              })
            } else if (i.quantity < copyOfCart[tmp].quantity) {
              this.cart.items[tmp].quantity = i.quantity
              localStorage.setItem('cart', JSON.stringify(this.cart))
              toast({
                message: `hurry, only ${i.quantity} units of the product ${i.name} are left`,
                type: "is-warning",
                position: "center",
                duration: 8000,
                pauseOnHover: true,
                dismissible: true,
              })
            }
          }
        }
      })
    },
    async getProductsList() {
      await axios.post('/api/v1/products/check/check/check-products/', {'productsList': this.productsList})
          .then(response => {
            this.checkedProducts = response.data
          })
          .catch(error => {
            console.log(error)
          })
    }
  },
}
</script>

<style scoped>

</style>
