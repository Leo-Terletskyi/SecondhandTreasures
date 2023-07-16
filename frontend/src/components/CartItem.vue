<template>
  <tr class="cart-item-tr">
    <td>
      <router-link :to="item.product.get_absolute_url">
        <span class="cart-item-url">{{ item.product.name }}</span>
      </router-link>
    </td>
    <td>
      ${{ item.product.price }}
    </td>
    <td>
      <span class="pr-4">
        {{ item.quantity }}
      </span>
      <a @click="decrementQuantity(item)" class="has-text-primary">
        <font-awesome-icon icon="fa-solid fa-minus"/>
      </a>
      <span></span>
    </td>
    <td>
      ${{ getItemTotal(item).toFixed(2) }}
    </td>
    <td>
      <button @click="removeFromCart(item)" class="has-background-danger">
        <font-awesome-icon icon="fa-solid fa-delete-left"/>
      </button>
    </td>
  </tr>
</template>


<script>

export default {
  name: 'CartItem',
  props: {
    initialItem: Object,
  },
  data() {
    return {
      item: this.initialItem
    }
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price
    },
    decrementQuantity(item) {
      item.quantity -= 1

      if (item.quantity === 0) {
        this.$emit('removeFromCart', item)
      }

      this.updateCart()
    },
    updateCart() {
      localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
    },
    removeFromCart(item) {
      this.$emit('removeFromCart', item)

      this.updateCart()
    },
  },
}
</script>

<style lang="scss" scoped>
.cart-item-tr {
  color: white;
}

.cart-item-url {
  color: gold;
}
</style>
