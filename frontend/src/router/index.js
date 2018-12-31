import Vue from 'vue'
import Router from 'vue-router'
import ReportSystem from '@/main.vue'
import ReportList from '@/views/ReportList'
// import PcReport from '@/views/PcReport'
// import PhoneReport from '@/views/PhoneReport'
import BugList from '@/views/BugList'
import DemandList from '@/views/DemandList'
import ReportEdit from '@/views/ReportEdit'

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
          path: '/report/edit',
          name: 'ReportEdit',
          component: ReportEdit,
          meta: {
            keepAlive: true
          }
        },
        // {
        //   path: '/pc_report',
        //   name: 'PcReport',
        //   component: PcReport,
        //   meta: {
        //     keepAlive: true
        //   }
        // },
        // {
        //   path: '/phone_report',
        //   name: 'PhoneReport',
        //   component: PhoneReport,
        //   meta: {
        //     keepAlive: true
        //   }
        // },
        {
          path: '/bug/list',
          name: 'BugList',
          component: BugList,
          meta: {
            keepAlive: true
          }
        },
        {
          path: '/demand/list',
          name: 'DemandList',
          component: DemandList,
          meta: {
            keepAlive: true
          }
        }
      ]
    }
  ],
  mode: "history",  //去掉地址栏的#号键
}) 
