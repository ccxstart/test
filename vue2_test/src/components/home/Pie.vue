<template>
  <div id="pie">
    <div>
      <el-row>
        <el-col :span="4">
          <div class="grid-content bg-purple">
            <el-select v-model="selectedProvince" @change="loadCities" placeholder="请选择省份">
              <el-option value="请选择省份">请选择省份</el-option>
              <el-option v-for="province in provinces" :key="province" :value="province">
              </el-option>
            </el-select>
          </div>
        </el-col>
        <el-col :span="4">
          <div class="grid-content bg-purple-light">
            <el-select v-model="selectedCity" @change="loadCitiesDowntown" placeholder="请选择市区">
              <el-option value="请选择市区">请选择市级</el-option>
              <el-option v-for="city in cities" :key="city" :value="city">
              </el-option>
            </el-select>
          </div>
        </el-col>
        <el-col :span="4">
          <div class="grid-content bg-purple-light">
            <el-select v-model="selectedDowntown" placeholder="请选择县级">
              <el-option value="请选择市区">请选择县级</el-option>
              <el-option v-for="downtown in downtowns" :key="downtown" :value="downtown">
              </el-option>
            </el-select>
          </div>
        </el-col>
        <el-col :span="8">
          <div class="grid-content bg-purple">
            <el-button type="primary" @click="searchData">搜索</el-button>
          </div>
        </el-col>
      </el-row>
    </div>
    <div id="main" style="width: 1000px;height:500px;"></div>
    <h1></h1>
  </div>
</template>

<script>
import * as echarts from 'echarts'
export default {
  name: 'Pie',
  mounted () {
    this.getProvinceList()
    // 基于准备好的dom，初始化echarts实例
    this.myChart = echarts.init(document.getElementById('main'))
    // 使用刚指定的配置项和数据显示图表。
    this.searchData()
  },
  data () {
    return {
      // myChart: echarts.init(document.getElementById('main')),
      queryInfo: {
        province: '',
        city: '',
        downtown: ''
      },
      selectedProvince: '北京',
      selectedCity: '北京',
      selectedDowntown: '大兴',
      provinces: [],
      cities: [],
      downtowns: [],
      data_list: []
    }
  },
  methods: {
    async getProvinceList () {
      this.queryInfo.province = this.selectedProvince
      this.queryInfo.province = this.selectedCity
      const { data: res } = await this.$axios.get('/home/data/province_list', { params: this.queryInfo })
      // console.log(res)
      this.provinces = res.data || []
    },
    async loadCities () {
      this.selectedCity = ''
      this.selectedDowntown = ''
      this.queryInfo.province = this.selectedProvince
      const { data: res } = await this.$axios.get('/home/data/city_list', { params: this.queryInfo })
      console.log(res)
      this.cities = res.data || []
    },
    async loadCitiesDowntown () {
      this.selectedDowntown = ''
      this.queryInfo.province = this.selectedProvince
      this.queryInfo.city = this.selectedCity
      const { data: res } = await this.$axios.get('/home/data/downtown_list', { params: this.queryInfo })
      console.log(res.data)
      this.downtowns = res.data || []
    },
    async searchData () {
      this.queryInfo.province = this.selectedProvince
      this.queryInfo.city = this.selectedCity
      this.queryInfo.downtown = this.selectedDowntown
      const { data: res } = await this.$axios.get('/home/data/pie', { params: this.queryInfo })
      console.log(res)
      this.option = {
        title: {
          text: '城市不同区域饼图',
          left: 'center',
          textStyle: {
            fontSize: 22, // 标题字体大小
            fontWeight: 'bold' // 标题字体粗细
          }
        },
        legend: {
          top: 'bottom'
        },
        tooltip: {
          trigger: 'item', // 触发类型为item，表示鼠标悬停在数据项上时显示
          formatter: '{b} : {c} ({d}%)' // 自定义提示框的内容，其中{c}表示数值，{d}%表示百分比
        },
        toolbox: {
          show: true,
          feature: {
            mark: {show: true},
            dataView: {show: true, readOnly: false},
            restore: {show: true},
            saveAsImage: {show: true}
          }
        },
        series: [
          {
            name: 'Nightingale Chart',
            type: 'pie',
            radius: [50, 200],
            center: ['50%', '50%'],
            roseType: 'area',
            itemStyle: {
              borderRadius: 5
            },
            data: res.data
            //   [
            //   {value: 40, name: 'rose 1'},
            //   {value: 38, name: 'rose 2'},
            //   {value: 32, name: 'rose 3'},
            //   {value: 30, name: 'rose 4'},
            //   {value: 28, name: 'rose 5'}
            //   // {value: 26, name: 'rose 6'},
            //   // {value: 22, name: 'rose 7'},
            //   // {value: 18, name: 'rose 8'}
            // ]
          }
        ]
      }
      this.option && this.myChart.setOption(this.option)
    }
  }
}
</script>

<style scoped lang="less">
#main {
  margin-top: 50px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%)
}
</style>
