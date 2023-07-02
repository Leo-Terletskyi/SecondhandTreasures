import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

/* import the fontawesome core */
import {library} from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'

/* import specific icons */
import {faCartShopping} from '@fortawesome/free-solid-svg-icons'
import {faUser} from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faCartShopping, faUser)


const secondhandTreasures = createApp(App)
secondhandTreasures.use(store)
secondhandTreasures.use(router)
secondhandTreasures.component('font-awesome-icon', FontAwesomeIcon)
secondhandTreasures.mount('#app')
