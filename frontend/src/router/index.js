import Vue from 'vue'
import Router from 'vue-router'
import ReportSystem from '@/main.vue'
import ReportList from '@/views/ReportList'
// import PcReport from '@/views/PcReport'
// import PhoneReport from '@/views/PhoneReport'
import BugList from '@/views/BugList'
import DemandList from '@/views/DemandList'
import ReportEdit from '@/views/ReportEdit'
import PcDetail from '@/views/PcDetail'
import AppDetail from '@/views/AppDetail'
import Login from '@/views/Login.vue'

Vue.use(Router)
mode: 'history'
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
        {
          path: '/report/detail/pc/:id',
          name: 'PcDetail',
          component: PcDetail,
          meta: {
            keepAlive: true
          }
        },
        {
          path: '/report/detail/app/:id',
          name: 'AppDetail',
          component: AppDetail,
          meta: {
            keepAlive: true
          }
        },
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
        },
      ],
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: {
        keepAlive: true
      },
    }
  ],
  mode: "history",  //去掉地址栏的#号键
}) 
