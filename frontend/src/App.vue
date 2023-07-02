<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <img src="./assets/logo-no-background.svg" alt="">
        </router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-menu" id="navbar-menu" :class="{'is-active': showMobileMenu}">
        <div class="navbar-end">
          <router-link to="" class="navbar-item">Link 1</router-link>
          <router-link to="" class="navbar-item">Link 2</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light">
                <font-awesome-icon icon="fa-solid fa-user" />
                <span class="px-2">
                  Log in
                </span>
              </router-link>
              <router-link to="/cart" class="button is-success">
                <font-awesome-icon icon="fa-solid fa-cart-shopping"/>
                <span class="px-2">Cart</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

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
export default {
  name: 'App',
  data() {
    return {
      showMobileMenu: false,
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
</style>
