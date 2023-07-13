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

import CartItem from "@/components/CartItem";

export default {
  name: 'CartView',
  components: {CartItem},
  data() {
    return {
      cart: {
        items: []
      }
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
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
    }
  }
}
</script>

<style scoped>

</style>
