<template>
  <div class="page">
    <div class="page__head box has-background-primary-light">
      <h2 class="title is-2">search by query <span style="color: gold">{{ query }}</span>:</h2>
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

import ProductCard from "@/components/ProductCard";
import {toast} from "bulma-toast";

export default {
  name: "SearchView",
  components: {
    ProductCard,
  },
  data() {
    return {
      products: [],
      query: '',
    }
  },
  mounted() {
    document.title = 'search'
    let url = window.location.search.substring(1)
    let params = new URLSearchParams(url)
    if (params.get('query')) {
      this.query = params.get('query')
      this.performSearch()
    }
    document.title = `search '${this.query}'`
  },
  methods: {
    async performSearch() {
      document.title = `category: ${this.category}`
      this.$store.commit('setIsLoading', true)
      await axios.post('/api/v1/products/search/', {'query': this.query})
          .then(response => {
            this.products = response.data
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