import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios"

axios.defaults.baseURL = 'http://127.0.0.1:8000'

/* import the fontawesome core */
import {library} from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'

/* import specific icons */
import {faCartShopping} from '@fortawesome/free-solid-svg-icons'
import {faUser} from '@fortawesome/free-solid-svg-icons'
import {faSearch} from "@fortawesome/free-solid-svg-icons/faSearch";

/* add icons to the library */
library.add(faCartShopping, faUser, faSearch)


const secondhandTreasures = createApp(App)
secondhandTreasures.use(store)
secondhandTreasures.use(router, axios)
secondhandTreasures.component('font-awesome-icon', FontAwesomeIcon)
secondhandTreasures.mount('#app')
