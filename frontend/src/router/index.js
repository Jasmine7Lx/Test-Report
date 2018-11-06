import Vue from 'vue'
import Router from 'vue-router'
import ReportSystem from '@/main.vue'
import ReportList from '@/components/ReportList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'ReportSystem',
      component: ReportSystem
    },
    {
      path: '/2',
      name: 'ReportList',
      component: ReportList
    }
  ],
  mode: "history"  //去掉地址栏的#号键
}) 
