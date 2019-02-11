<template>
<div>
    <div class="d1">
        <el-select v-model="select_show">
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
  export default {
    data() {
      return {
        select_show: 'myself',
        showlist: [{
          value: 'myself',
          label: '只查看自己'
          }, {
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