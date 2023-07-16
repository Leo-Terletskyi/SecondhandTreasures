<template>
  <div class="page">
    <div class="page__head box has-background-primary-light">
      <h2 class="title is-2">Find your <span style="color: gold">Treasure</span></h2>
      <h4 class="title is-4">Latest products in category <span style="color: green">{{ category }}:</span></h4>
    </div>
    <div class="page__body">
      <div class="columns is-multiline is-mobile">
        <ProductCard
          v-for="product in products"
          :key="product.id"
          :product="product"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {toast} from "bulma-toast";

import ProductCard from "@/components/ProductCard";

export default {
  name: "CategoryPage",
  components: {
    ProductCard
  },
  data() {
    return {
      category: '',
      products: []
    }
  },
  mounted() {
    this.getProducts()
  },
  watch: {
    $route(to, from) {
      if (to.name === 'categoryPage') {
        this.getProducts()
      }
    }
  },
  methods: {
    async getProducts() {
      this.category = this.$route.params.category_slug,
      document.title = `category: ${this.category}`
      this.$store.commit('setIsLoading', true)
      await axios.get(`/api/v1/products/${this.category}`)
          .then(response => {
            this.products = response.data.products
          })
          .catch(err => {
            console.log(err)
            toast({
              message: 'Something going wrong',
              type: "is-warning",
              position: "top-center",
              duration: 2000,
              pauseOnHover: true,
              dismissible: true,
            })
          })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style scoped>
</style>
