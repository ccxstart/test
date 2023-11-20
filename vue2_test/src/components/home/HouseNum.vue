<template>
  <div id="house">
<!--    <h1>HouseNum</h1>-->
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
          <el-select v-model="selectedCity" placeholder="请选择市区">
            <el-option value="请选择市区">请选择市级</el-option>
            <el-option v-for="city in cities" :key="city" :value="city">
            </el-option>
          </el-select>
        </div>
      </el-col>
        <el-col :span="4">
          <div class="grid-content bg-purple-light">
            <el-button type="primary" @click="searchData">搜索</el-button>
          </div>
        </el-col>
      </el-row>
    </div>
    <el-row class="row_span">
      <el-col :span="12">
        <div id="left" style="height:500px;"></div>
      </el-col>
      <el-col :span="12">
        <div id="right" style="height:500px;"></div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  name: 'HouseNum',
  mounted () {
    this.getProvinceList()
    this.rightChart = echarts.init(document.getElementById('right'))
    this.leftChart = echarts.init(document.getElementById('left'))
    this.searchData()
  },
  data () {
    return {
      selectedProvince: '北京',
      selectedCity: '北京',
      provinces: [],
      cities: [],
      queryInfo: {
        province: '',
        city: ''
      }
    }
  },
  methods: {
    async getProvinceList () {
      this.queryInfo.province = this.selectedProvince
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
      console.log(this.selectedProvince)
      this.queryInfo.province = this.selectedProvince
      this.queryInfo.city = this.selectedCity
      const { data: res } = await this.$axios.get('/home/data/houseNum', { params: this.queryInfo })
      console.log(res)
      const rightOption = {
        title: {
          text: '房源数量柱状图', // 标题文本
          left: 'center', // 标题水平居中
          top: 'top', // 标题距离顶部的距离
          textStyle: {
            fontSize: 22, // 标题文字大小
            fontWeight: 'bold' // 标题文字粗细
          }
        },
        // abscissa : 横坐标       ordinate : 纵坐标
        xAxis: {
          type: 'category',
          data: res.data.right.x_right,
          axisLabel: {
            interval: 0, // 设置标签的显示间隔为0，表示全部显示
            rotate: 45 // 标签的旋转角度，如果需要的话
          }
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            data: res.data.right.y_right,
            type: 'bar',
            // 设置柱子的形状，例如圆角
            itemStyle: {
              borderRadius: [22, 22, 22, 22] // 数组中的四个值分别代表左上、右上、右下、左下的圆角程度
              // color: 'pink'
            }
          }
        ],
        tooltip: {
          show: true, // 启用提示框
          trigger: 'axis', // 触发类型，这里设置为 'axis' 表示鼠标悬浮在坐标轴上时触发
          formatter: '{b}: {c}' // 提示框内容格式，{b} 表示横坐标值，{c} 表示数据值
        }
      }
      const leftOption = {
        title: {
          text: '房源数量饼图', // 标题文本
          left: 'center', // 标题水平居中
          top: 'top', // 标题距离顶部的距离
          textStyle: {
            fontSize: 22, // 标题文字大小
            fontWeight: 'bold' // 标题文字粗细
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
            radius: [50, 170],
            center: ['50%', '50%'],
            roseType: 'area',
            itemStyle: {
              borderRadius: 8
            },
            data: res.data.left
            // data: [
            //   {value: 40, name: 'rose 1'},
            //   {value: 38, name: 'rose 2'},
            //   {value: 32, name: 'rose 3'},
            //   {value: 30, name: 'rose 4'},
            //   {value: 28, name: 'rose 5'},
            //   {value: 26, name: 'rose 6'},
            //   {value: 22, name: 'rose 7'},
            //   {value: 18, name: 'rose 8'}
            // ]
          }
        ]
      }
      rightOption && this.rightChart.setOption(rightOption)
      leftOption && this.leftChart.setOption(leftOption)
    }
  }
}
</script>

<style scoped lang="less">
.row_span {
  margin-top: 20px;
}
#right {
  border-left: 1px solid pink;
  margin-left: 2px;
}
</style>
