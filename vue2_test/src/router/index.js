import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login'
import Home from '../components/Home'
import Data from '../components/home/Data'
import Splattering from '../components/home/Splattering'
import Pie from '../components/home/Pie'
import HouseNum from '../components/home/HouseNum'
import AveragerRent from '../components/home/AveragerRent'
import ChinaMap from '@/components/home/ChinaCharts'
import Admin from '../components/logs/Admin'

import * as echarts from 'echarts'
import chinaMap from '@/assets/map/china.json'
import * as d3 from 'd3'

echarts.registerMap("中国", chinaMap)
echarts.registerMap("china", chinaMap)

export { chinaMap, echarts, d3 }

// import echarts from 'echarts'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    component: Login
  },
  {
    path: '/',
    component: Login
  },
  {
    path: '/home',
    name: 'home',
    component: Home,
    redirect: '/home/data',
    children: [
      {
        path: '/home/data', component: Data
      },
      {
        path: '/home/average', component: Splattering
      },
      {
        path: '/home/pie', component: Pie
      },
      {
        path: '/home/house', component: HouseNum
      },
      {
        path: '/home/averagerRent', component: AveragerRent
      },
      {
        path: '/home/map', component: ChinaMap
      },
      {
        path: '/home/admin', component: Admin
      }
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router

router.beforeEach((to, from, next) => {
  if (to.path === '/login') return next()
  const tokenStr = window.sessionStorage.getItem('token')
  if (!tokenStr) return next('/login')
  next()
})

// import Map_110000 from '@/assets/map/province/北京市_110000.json'
// import Map_120000 from '@/assets/map/province/天津市_120000.json'
// import Map_130000 from '@/assets/map/province/河北省_130000.json'
// import Map_140000 from '@/assets/map/province/山西省_140000.json'
// import Map_150000 from '@/assets/map/province/内蒙古自治区_150000.json'
// import Map_210000 from '@/assets/map/province/辽宁省_210000.json'
// import Map_220000 from '@/assets/map/province/吉林省_220000.json'
// import Map_230000 from '@/assets/map/province/黑龙江省_230000.json'
// import Map_310000 from '@/assets/map/province/上海市_310000.json'
// import Map_320000 from '@/assets/map/province/江苏省_320000.json'
// import Map_330000 from '@/assets/map/province/浙江省_330000.json'
// import Map_340000 from '@/assets/map/province/安徽省_340000.json'
// import Map_350000 from '@/assets/map/province/福建省_350000.json'
// import Map_360000 from '@/assets/map/province/江西省_360000.json'
// import Map_370000 from '@/assets/map/province/山东省_370000.json'
// import Map_410000 from '@/assets/map/province/河南省_410000.json'
// import Map_420000 from '@/assets/map/province/湖北省_420000.json'
// import Map_430000 from '@/assets/map/province/湖南省_430000.json'
// import Map_440000 from '@/assets/map/province/广东省_440000.json'
// import Map_450000 from '@/assets/map/province/广西壮族自治区_450000.json'
// import Map_460000 from '@/assets/map/province/海南省_460000.json'
// import Map_500000 from '@/assets/map/province/重庆市_500000.json'
// import Map_510000 from '@/assets/map/province/四川省_510000.json'
// import Map_520000 from '@/assets/map/province/贵州省_520000.json'
// import Map_530000 from '@/assets/map/province/云南省_530000.json'
// import Map_540000 from '@/assets/map/province/西藏自治区_540000.json'
// import Map_610000 from '@/assets/map/province/陕西省_610000.json'
// import Map_620000 from '@/assets/map/province/甘肃省_620000.json'
// import Map_630000 from '@/assets/map/province/青海省_630000.json'
// import Map_640000 from '@/assets/map/province/宁夏回族自治区_640000.json'
// import Map_650000 from '@/assets/map/province/新疆维吾尔自治区_650000.json'
// import Map_810000 from '@/assets/map/province/香港_810000.json'
// import Map_820000 from '@/assets/map/province/澳门_820000.json'
//
//
// echarts.registerMap("110000", Map_110000)
// echarts.registerMap("120000", Map_120000)
// echarts.registerMap("130000", Map_130000)
// echarts.registerMap("140000", Map_140000)
// echarts.registerMap("150000", Map_150000)
// echarts.registerMap("210000", Map_210000)
// echarts.registerMap("220000", Map_220000)
// echarts.registerMap("230000", Map_230000)
// echarts.registerMap("310000", Map_310000)
// echarts.registerMap("320000", Map_320000)
// echarts.registerMap("330000", Map_330000)
// echarts.registerMap("340000", Map_340000)
// echarts.registerMap("350000", Map_350000)
// echarts.registerMap("360000", Map_360000)
// echarts.registerMap("370000", Map_370000)
// echarts.registerMap("410000", Map_410000)
// echarts.registerMap("420000", Map_420000)
// echarts.registerMap("430000", Map_430000)
// echarts.registerMap("440000", Map_440000)
// echarts.registerMap("450000", Map_450000)
// echarts.registerMap("460000", Map_460000)
// echarts.registerMap("500000", Map_500000)
// echarts.registerMap("510000", Map_510000)
// echarts.registerMap("520000", Map_520000)
// echarts.registerMap("530000", Map_530000)
// echarts.registerMap("540000", Map_540000)
// echarts.registerMap("610000", Map_610000)
// echarts.registerMap("620000", Map_620000)
// echarts.registerMap("630000", Map_630000)
// echarts.registerMap("640000", Map_640000)
// echarts.registerMap("650000", Map_650000)
// echarts.registerMap("810000", Map_810000)
// echarts.registerMap("820000", Map_820000)
