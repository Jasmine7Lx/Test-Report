<template>
    <div>
        <div style="margin:2% 0">
            <el-radio v-model="type" @change="handleChange" label="PC端报告"></el-radio>
            <el-radio v-model="type" @change="handleChange" label="移动端报告"></el-radio>
        </div>
    <pc-report v-if="type=='PC端报告'"></pc-report>
    <phone-report v-if="type=='移动端报告'" ></phone-report>
    </div>
</template>

<script>
import PcReport from './PcReport'
import PhoneReport from './PhoneReport'
export default {
    components: {
        PcReport, PhoneReport
    },
    data(){
        return {
            type: "PC端报告"
        }
    },
    methods:{
        handleChange(val){
            if (val=="PC端报告"){
                this.type = "PC端报告"
            } else{
                this.type = "移动端报告"
            }
        }
    }
}
</script>

<style>

</style>