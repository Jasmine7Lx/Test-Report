<template>
<div>
    <div class="d1">
        <el-select v-model="select_show" @change="onSeleteShow">
          <el-option
            v-for="item in showlist"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
    </div>
    <div style="padding-top: 45px">
      <hr />
    </div>
</div>
</template>

<script>
import https from '../../https.js'
  export default {
    data() {
      return {
        changeList: [],
        select_show: 'all',
        showlist: [{
            value: 'all',
            label: '查看全部'
          }, {
            value: 'pclist',
            label: '查看pc端报告'
          }, {
            value: 'phonelist',
            label: '查看移动端报告'
          }
        ]
      }
    },
    methods: {
      onSeleteShow: function(item){
        if(item=="all"){
          https.fetchGet('/api/reportlistall')
          .then((resp) => {
            console.log(resp.data)
            this.reportList = resp.data.reportlist
          })
        }
        else if(item=="pclist"){
          https.fetchGet('/api/reportlistpc')
          .then((resp) => {
            console.log(resp.data)
            this.reportList = resp.data.reportlist
          })
        }
      }
    }
  }
</script>

<style>
.d1{
  float: left;
  padding-left: 5px;
}

.check {
    display: inline-block;
    padding-left: 15px;
    padding-top: 5px;
}
</style>