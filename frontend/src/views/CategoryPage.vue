<template>
  <div class="page">
    <div class="page__head box has-background-primary-light">
      <h2 class="title is-2">Find your <span style="color: gold">Treasure</span></h2>
      <h4 class="title is-4">Latest products in category <span style="color: green">{{ category }}:</span></h4>
    </div>
    <div class="page__body">
      <div class="columns is-multiline is-desktop">
        <div class="column is-2" v-for="product in products" :key="product.id">
          <div class="card p-1">
            <div class="card-image">
              <figure class="image is-3by4">
                <img :src="product.image.medium_square_crop" alt="">
              </figure>
            </div>
            <div class="card-content p-3">
              <div class="media">
                <div class="media-content">
                  <p class="title is-4">{{ product.name }}</p>
                  <p class="subtitle is-6">{{ product.category_name }}</p>
                </div>
              </div>

              <div class="content">
                <div class="product-description" v-if="product.description">
                  <hr>
                  <p>{{ product.description }}</p>
                </div>
                <div class="product-description" v-else>
                  <hr>
                  <p>...</p>
                </div>
              </div>
            </div>
            <div class="card-footer">
              <div class="field">
                <div class="control is-expanded pt-2"><strong><span style="color: #42b983">$</span> {{ product.price }}</strong></div>
                <div class="control">
                  <router-link :to="product.get_absolute_url">
                    <button class="button is-primary">Detail..</button>
                  </router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {toast} from "bulma-toast";

export default {
  name: "CategoryPage",
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
      document.title = 'SecondhandTreasures'
      this.$store.commit('setIsLoading', true)
      await axios.get(`/api/v1/${this.category}`)
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
.field {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.card {
  display: flex;
  flex-direction: column;
  height: 100%;

}

.card-footer {
  display: block;
  margin-top: auto;
}
</style>
