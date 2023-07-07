<template>
  <div class="page">
    <div class="page__head box has-background-primary-light">
      <h2 class="title is-2">Find your <span style="color: gold">Treasure</span></h2>
      <h4 class="title is-4">Latest products:</h4>
    </div>
    <div class="page__body">
      <div class="columns is-multiline is-desktop">
        <ProductCard
          v-for="product in latestProducts"
          :key="product.id"
          :product="product"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"

import ProductCard from "@/components/ProductCard";

export default {
  name: 'Home',
  components: {
    ProductCard,
  },
  data() {
    return {
      latestProducts: [],
    }
  },
  mounted() {
    this.getLatestProducts()
  },
  methods: {
    async getLatestProducts() {
      document.title = 'SecondhandTreasures'
      this.$store.commit('setIsLoading', true)
      await axios
          .get('/api/v1/latest-products')
          .then(response => {
            this.latestProducts = response.data
          })
          .catch(error => {
            console.log(error)
          })
      this.$store.commit('setIsLoading', false)
    },
  }
}
</script>

<style lang="scss" scoped>
</style>