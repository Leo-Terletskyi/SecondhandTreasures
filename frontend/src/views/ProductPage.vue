<template>
  <div class="product-page">
    <div class="box">
      <div class="columns">
        <div class="column is-two-thirds">
          <div class="columns">
            <div class="column is-half">
              <figure class="image">
                <img :src="image.full_size" alt="">
              </figure>
            </div>
            <div class="column is-half">
              <h3 class="title">{{ product.name }}</h3>
              <div class="content">
                <div class="product-description" v-if="product.description">
                  <hr>
                  <p>{{ product.description }}</p>
                  <hr>
                </div>
                <div class="product-description" v-else>
                  <hr>
                  <p>...</p>
                  <hr>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="column is-one-third">
          <div class="box" style="height: 100%">
            <h3 class="title is-4 has-text-centered has-text-success mb-6">Price: ${{ product.price }}</h3>
            <div class="add-to-cart">
              <div class="add-to-cart__input">
                <input class="input" type="number" min="1" v-model="quantity">
              </div>
              <div class="add-to-cart__button" v-if="product.quantity > productsAdded">
                <button type="button" class="button is-success" @click="addToCart">Add to cart</button>
              </div>
              <div class="add-to-cart__button" v-else>
                <button type="button" class="button is-dark">the product is out of stock</button>
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
import {toast} from 'bulma-toast'

export default {
  name: "ProductPage",
  data() {
    return {
      cart: {
        items: []
      },
      product: {},
      image: '',
      quantity: 1,
      productsAdded: 0
    }
  },
  async mounted() {
    await this.getProduct()
    await this.getCorrectQuantityCart()
  },
  methods: {
    async getProduct() {
      this.$store.commit('setIsLoading', true)
      const category_slug = this.$route.params.category_slug
      const product_slug = this.$route.params.product_slug

      await axios
          .get(`/api/v1/products/${category_slug}/${product_slug}`)
          .then(response => {
            this.product = response.data
            this.image = this.product.image
            document.title = this.product.name
          })
          .catch(error => {
            console.log(error)
          })
      this.$store.commit('setIsLoading', false)
      console.log(this.$store.state.isLoading)
    },
    getCorrectQuantityCart() {
      this.cart = this.$store.state.cart
      this.cart.items.forEach((i) => {
        if (i.product.id === this.product.id) {
          this.productsAdded = i.quantity
        }
      })
    },
    addToCart() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1
      }
      const item = {
        product: this.product,
        quantity: this.quantity
      }
      if (item.product.quantity < item.quantity) {
        item.quantity = item.product.quantity
      }
      this.productsAdded += this.quantity
      this.$store.commit('addToCart', item)
      toast({
        message: 'The product was added to the cart',
        type: "is-success",
        position: "bottom-right",
        duration: 2000,
        pauseOnHover: true,
        dismissible: true,
      })
    }
  }
}
</script>


<style lang="scss" scoped>
.add-to-cart {
  display: flex;
  justify-content: center;

  &__input {

  }

  &__button {
    color: red;
  }
}
</style>