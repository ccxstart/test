<template>
  <div>
    <div id="splattering">
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
    <div id="main" style="width: 1000px;height:500px;">
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  name: 'Splattering',
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
      selectedProvince: '北京',
      selectedCity: '北京',
      selectedDowntown: '大兴',
      queryInfo: {
        province: '',
        city: '',
        downtown: ''
      },
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
      const { data: res } = await this.$axios.get('/home/data/splattering', { params: this.queryInfo })
      // console.log(res.data)
      if (res.status !== 200) return this.$msg.error(res.msg)
      this.data_list = res.data
      // console.log(res.data)
      this.myChart.setOption({
        title: {
          text: '城市不同区域散点图', // 设置标题文本
          left: 'center', // 标题居中对齐
          textStyle: {
            // 设置字体大小
            fontSize: 30
          }
        },
        xAxis: {
          name: '面积/㎡'
        },
        yAxis: {
          name: '租金/元'
        },
        series: [
          {
            symbolSize: 20,
            data: res.data,
            type: 'scatter'
          }
        ],
        tooltip: {
          trigger: 'item', // 触发类型为数据项
          formatter: function (params) {
            // console.log(params)
            return '面积: ' + params.data[0] + '㎡' + '---' + '租金' + params.data[1] + '元' // 显示信息
          }
        }
      })
      // console.log(this.queryInfo.province)
      // console.log(this.selectedCity)
    }
  }
}
</script>

<style scoped lang="less">
#main {
  margin-top: 60px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%)
}
</style>
