// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App'
import router from './router'
import axios from 'axios'
import QS from 'qs'
import Moment from 'moment'

Vue.config.productionTip = false
Vue.prototype.$axios = axios
Vue.prototype.qs = QS
Vue.prototype.moment = Moment
// Vue.filter('dateFmt', (input, formatString = "YYYY-MM-DD") => {
//   //es5函数参数设置默认值    
//   //const lastFormatString = formatString || ''         
//   //moment(input) 把时间字符串转成时间对象     
//   //format(formatString) 把时间对象，按照指定格式，格式化成符合条件的字符串
//   return Moment(input).format(formatString)
// })


Vue.use(ElementUI)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
