<template>
  <template v-if="product.quantity > 0">
    <div class="column is-12-mobile is-one-third-tablet is-one-fifth-desktop">
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
              <p class="product-description__desript">{{ product.description }}</p>
            </div>
            <div class="product-description" v-else>
              <hr>
              <p>...</p>
            </div>
          </div>
        </div>
        <div class="card-footer">
          <div class="field">
            <div class="control is-expanded mt-3"><strong><span style="color: #42b983">$</span> {{ product.price }}</strong></div>
            <div class="control">
              <router-link :to="product.get_absolute_url">
                <button class="button is-primary mt-1 p-2">Detail..</button>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
</template>

<script>
export default {
  name: "ProductCard",
  props: {
    product: Object
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

.product-description__desript {
  max-height: 100px;
  overflow: hidden;
}
</style>
