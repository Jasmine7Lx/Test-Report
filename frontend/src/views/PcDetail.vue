<template>
  <div class="edit">
    <h1>测试结论：</h1>
    <h1>遗留问题：</h1>
    <span style="font-size:16.5px; padding-left:10px;">三、测试说明：</span>
        <el-row>
            <span class="explain">1.测试环境：</span>
        </el-row >
        <el-row>
            <span class="explain">2.环境配置：</span>
        </el-row>
        <el-row>
            <span class="explain">3.测试版本/链接：</span>
        </el-row>
        <el-row>
            <span class="explain">4.测试时间：</span>
        </el-row>
    <span style="font-size:16.5px; padding-left:10px;">四、测试中发现的问题：</span>
        <el-row>
            <span class="explain">1.前端bug：</span>
        </el-row>
        <el-row>
            <span class="explain">2.后端bug：</span>
        </el-row>
    <span style="font-size:16.5px; padding-left:10px;">五、兼容性：</span>
        <el-row>
            <el-col>
                <span class="explain">1.电脑系统：</span>
            </el-col>
        </el-row>
        <el-row>
            <el-col>
                <span class="explain">2.浏览器：</span>
            </el-col>
        </el-row>
    <span style="font-size:16.5px; padding-left:10px;">六、测试用例：</span>
        <span class="explain">链接：</span>
        <span class="explain">文件：</span>
    </div>
</template>
<script>
import https from '../https.js'
export default {
    data() {
        return {

        }
    },
    methods: {
        getReportDetail: function() {
            let reportId = this.$route.params.id;
            console.log(reportId)
            https.fetchGet('api/pcreport', {params:{id: reportId}})
            .then((resp) => {
                let data = resp.data
            })
        }
    },
    created() {
        this.getReportDetail()
    }
}
</script>
