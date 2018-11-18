<template>
<div>
   <div>
       <date-check></date-check>
   </div>
   <div>
   <show-list></show-list>
   </div>
</div>
</template>

<script>
  import DateCheck from '@/components/ReportList/DateCheck'
  import ShowList from '@/components/ReportList/ShowList'
  export default {
    components: {
      'dateCheck': DateCheck,
      'showList': ShowList,
    },
  }
</script>

<style>

</style>
