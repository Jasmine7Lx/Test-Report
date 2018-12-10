import Vue from 'vue'
import Router from 'vue-router'
import ReportSystem from '@/main.vue'
import ReportList from '@/views/ReportList'
import Pc_Report from '@/views/Pc_Report'
import Phone_Report from '@/views/Phone_Report'
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
          path: '/pc_report',
          name: 'Pc_Report',
          component: Pc_Report,
          meta: {
            keepAlive: true
          }
        },
        {
          path: '/phone_report',
          name: 'Phone_Report',
          component: Phone_Report,
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
