<template>
<div>
  <el-table :data="tableData">
    <el-table-column prop="date" label="创建时间" width="250">
    </el-table-column>
    <el-table-column prop="name" label="需求名称" width="400">
    </el-table-column>
    <el-table-column prop="address" label="报告人">
    </el-table-column>
    </el-table> 
</div>  
</template>

<script>
export default {
    data() {
        const item = {
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        };
        return {
          tableData: Array(10).fill(item)
        }
    }
}
</script>

