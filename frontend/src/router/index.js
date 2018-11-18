import Vue from 'vue'
import Router from 'vue-router'
import ReportSystem from '@/main.vue'
import ReportList from '@/views/ReportList'
import ReportEdit from '@/views/ReportEdit'
import BugList from '@/views/BugList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: '报告列表',
      component: ReportSystem, 
      meta: {
        keepAlive: true
      },
      children:[
        {
          path: '/',
          name: 'ReportList',
          component: ReportList,
          meta: {
            keepAlive: true
          }
        },
        {
          path: '/reportedit',
          name: 'ReportEdit',
          component: ReportEdit,
          meta: {
            keepAlive: true
          }
        },
        {
          path: '/buglist',
          name: 'BugList',
          component: BugList,
          meta: {
            keepAlive: true
          }
        }
      ]
    }
  ],
  mode: "history",  //去掉地址栏的#号键
}) 
