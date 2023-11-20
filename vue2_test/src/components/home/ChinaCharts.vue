<template v-loading="true">
    <el-container
      v-loading="chartsInfo.loading"
      element-loading-text="加载地图中..."
      element-loading-spinner="el-icon-loading"
      class="chart-container" ref="chart"
    >
    </el-container>
</template>

<script>

export default {
  name: 'ChinaCharts',
  data() {
    return {
      data: [],
      chartsInfo: {
        loading: true
      },
      map: 'china',
    }
  },
  props: ["data", "title", "seriesName"],
  methods: {
    changeCharts(data, title) {
      data = data ? data : {min: null, max: null, data: null}
      const myCharts = this.$echarts.init(document.querySelector('.chart-container'))
      myCharts.off('click')
      const projection = this.$d3.geoAlbersUsa();
      const options = {
        title: {
          text: title,
          left: 'center',
          textStyle: {
            color: '#333333',
            fontWeight: 'bold',
            fontSize: 30
          }
        },
        tooltip: {
          trigger: 'item',
          showDelay: 0,
          transitionDuration: 0.2
        },
        visualMap: {
          left: 'right',
          min: data.min,
          max: data.max,
          inRange: {
            color: [
              '#313695',
              '#4575b4',
              '#74add1',
              '#abd9e9',
              '#e0f3f8',
              '#ffffbf',
              '#fee090',
              '#fdae61',
              '#f46d43',
              '#d73027',
              '#a50026'
            ]
          },
          text: ['最高', '最低'],
          calculable: true
        },
        series: [
          {
            name: this.title,
            type: "map",
            map: 'china',
            roam: true,
            zoom: 1.5,
            center: [106.35762, 35.287019],
            itemStyle: {
              color: 'rgba(255, 255, 255, 0.5)',
              opacity: 1
            },
            emphasis: {
              label: {
                show: true
              },
              itemStyle: {
                color: 'rgba(255, 255, 255, 1)',
                opacity: 1
              }
            },
            data: data.data,
          }
        ],

      }

      myCharts.setOption(options, true)
      myCharts.on("click", (params) => {
        let cityCode = this.$cityData[params.name]
        if (!cityCode) {
          this.$alert('暂无' + params.name + '地图数据', '错误提示', {
            confirmButtonText: '确定',
            callback: action => {
              this.$message({
                type: 'error',
                message: `action: ${action}`
              });
            }
          });
        } else {
          this.$router.push({name: "SalaryByCityMap", params: {city: params.name}})
        }

      }
      );

    }
  },
  mounted() {
    this.changeCharts(null, '全国各地租平均租房价格',)
    this.$axios.get('/home/data/map').then(rep => {
      this.data = rep.data
      this.changeCharts(this.data, '全国各地租平均租房价格',)
    }).finally(() => {
          setTimeout(() => {
            this.chartsInfo.loading = false
          }, 1000)
        }
    )
  }
}
</script>

<style scoped>
.chart-container {
  width: 100%;
  height: 85vh;
}
</style>
