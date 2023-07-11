<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <img src="./assets/white-and-gold.png" alt="">
        </router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu"
           @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-menu" id="navbar-menu" :class="{'is-active': showMobileMenu}">
        <div class="navbar-end">
          <div class="navbar-item mr-4">
            <form action="/search" method="get">
              <div class="field has-addons">
                <div class="control">
                  <input class="input" type="text" placeholder="Find a product" name="query">
                </div>
                <div class="control">
                  <button class="button is-gold" type="submit">
                    <font-awesome-icon icon="fa-solid fa-search"/>
                  </button>
                </div>
              </div>
            </form>
          </div>
          <div class="navbar-item has-dropdown is-hoverable mr-4">
            <a class="navbar-link">
              Categories
            </a>
            <div class="navbar-dropdown">
              <div class="navbar-item dropdown-item" v-for="category in allCategories" :key="category.id">
                <div class="cats">
                  <router-link :to="category.get_absolute_url" class="cat-name is-primary">
                    {{ category.name }}
                  </router-link>
                  <span class="cat-products-count has-text-success">
                      {{ category.products_count }}
                    </span>
                </div>
              </div>
            </div>
          </div>

          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light">My account</router-link>
              </template>
              <template v-else>
                <router-link to="/log-in" class="button is-success">
                  <font-awesome-icon icon="fa-solid fa-user"/>
                  <span class="px-2">
                  Log in
                </span>
                </router-link>
              </template>
              <router-link to="/cart" class="button is-gold">
                <font-awesome-icon icon="fa-solid fa-cart-shopping"/>
                <span style="margin-left: 10px">Cart ({{ cartTotalLength }})</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>


    <div class="is-loading-bar has-text-centered" :class="{'is-loading': $store.state.isLoading}">
      <div class="progress progress-infinite">
        <div class="progress-bar3">
        </div>
      </div>
    </div>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered">
        Copyright (c) 2023
      </p>
    </footer>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'App',
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: [],
      },
      allCategories: []
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
    this.getAllCategories()
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0
      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }
      return totalLength
    }
  },
  methods: {
    async getAllCategories() {
      await axios
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


<style lang="scss">
@import "../node_modules/bulma";

#app {
  min-height: 100vh;
}

#wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.section {
  flex: 1 0 auto;
}

.footer {
  max-height: 50px;
  padding: 15px;
}

.cats {
  width: 100%;
  display: flex;
  justify-content: space-between;
  font-size: 15px;
}

/*Loading Bar*/
.progress {
  padding: 6px;
  background: rgba(0, 0, 0, 0.25);
  border-radius: 6px;
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.25), 0 1px rgba(255, 255, 255, 0.08);
}

$green: #4cd964;
$turquoise: #5ac8fa;
$blue: #007aff;
$light-blue: #7DC8E8;
$purple: #5856d6;
$red: #ff2d55;

.progress-bar3 {
  height: 18px;
  border-radius: 4px;
  background-image: linear-gradient(to right,
      $green, $turquoise, $blue,
      $light-blue, $purple, $red);
  transition: 0.4s linear;
  transition-property: width, background-color;
}

.progress-infinite .progress-bar3 {
  width: 100%;
  background-image: linear-gradient(to right, $green, $turquoise, $blue, $light-blue, $purple, $red);
  animation: colorAnimation 1s infinite;
}

@keyframes colorAnimation {
  0% {
    background-image: linear-gradient(to right, $green, $turquoise, $blue, $light-blue, $purple, $red);
  }
  20% {
    background-image: linear-gradient(to right, $turquoise, $blue, $light-blue, $purple, $red, $green);
  }
  40% {
    background-image: linear-gradient(to right, $blue, $light-blue, $purple, $red, $green, $turquoise);
  }
  60% {
    background-image: linear-gradient(to right, $light-blue, $purple, $red, $green, $turquoise, $blue);
  }
  100% {
    background-image: linear-gradient(to right, $purple, $red, $green, $turquoise, $blue, $light-blue);
  }
}

.is-loading-bar {
  height: 0;
  width: 50%;
  margin: 0 auto;
  overflow: hidden;
  transition: all 0.3s;

  &.is-loading {
    height: auto;
  }
}

.is-gold {
  background: gold;
  border: none;
}

</style>
