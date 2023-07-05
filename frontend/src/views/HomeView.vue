<template>
  <div class="homepage">
    <div class="homepage__head box has-background-primary-light">
      <h2 class="title is-2">Find your <span style="color: gold">Treasure</span></h2>
      <h4 class="title is-4">Latest products:</h4>
    </div>
    <div class="homepage__body">
      <div class="columns is-multiline is-desktop">
        <div class="column is-2" v-for="product in latestProducts" :key="product.id">
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
import axios from "axios"

export default {
  name: 'Home',
  data() {
    return {
      latestProducts: [],
      allCategories: [],
    }
  },
  mounted() {
    this.getLatestProducts()
    this.getAllCategories()
  },
  methods: {
    async getLatestProducts() {
      document.title = 'Home page | Magazine'
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
    getAllCategories() {
      axios
          .get('/api/v1/all-categories')
          .then(response => {
            this.allCategories = response.data
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}
</script>

<style lang="scss" scoped>
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