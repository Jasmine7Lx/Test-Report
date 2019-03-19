<template>
<div>
  <div :class="className" :id="id" :style="{height:height,width:width}" ref="myEchart">
  </div>
</div>
</template>
<script>
import echarts from 'echarts'
import https from '../https.js'
export default {
  props: {
    className: {
      type: String,
      default: 'yourClassName'
    },
    id: {
      type: String,
      default: 'yourID'
    },
    width: {
      type: String,
      default: '1000px'
    },
    height: {
      type: String,
      default: '500px'
    }
  },
  data() {
    return {
      chart: null,
      bugList: [],
      serie: [],
      x: []
    }
  },
  mounted() {
    this.initChart();
    window.addEventListener("resize", () => {
      this.chart.resize();
    })
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose();
    this.chart = null;
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$refs.myEchart);
      // 把配置和数据放这里
      this.chart.setOption({
        title: {
          text: 'bug统计',
          x:'left',
          y:'top',
          textStyle: {
            fontSize: 18,
            color: '#333'
          }
        },
        color: ['#3398DB'],
        tooltip: {
          trigger: 'axis',
          axisPointer: { // 坐标轴指示器，坐标轴触发有效
            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
          }
        },
        grid: {
          left: '3%',
          right: '2%',
          bottom: '13%',
          containLabel: true
        },
        xAxis: [{
          type: 'category',
          data: this.x,
          axisTick: {
            alignWithLabel: true,
          },
          axisLabel: {
            show:true,
            textStyle:{fontSize:18}
          }
        }],
        yAxis: [{
          type: 'value',
          axisLabel: {
            show:true,
            textStyle:{fontSize:18}
          }
        }],
        series: [{
          name: 'bug数量',
          type: 'bar',
          barWidth: '60%',
          data: this.serie
        }]
      })
    },
    queryData() {
      https.fetchGet('/api/buglist')
      .then((resp => {
        for(var i=0; i<resp.data.series.length; i++) {
            this.serie[i] = resp.data.series[i].count
            this.x[i] = resp.data.series[i].name
          }
          this.$nextTick(() => { this.initChart() })
        }
      ))
    },
  },
  created() {
    this.queryData()
  },
}
</script>
