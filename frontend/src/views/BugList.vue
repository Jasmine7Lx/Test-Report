<template>
    <h1>{{bugList}}</h1>
</template>

<script>
import https from '../https.js'
export default {
    data() {
        return {
            bugList: []
        }
    },
    methods: {
        getBugs: function() {
          https.fetchGet('/api/buglist')
          .then((resp) => {
            console.log(resp)
            this.bugList = resp.data.data;
          })
        },
    },
    created() {
        this.getBugs()
    }
}
</script>
