<template>
  <div>
    <h2>書籍一覧</h2>
    <ul id="example-1">
      <li v-for="item in items" :key="item.message">
        {{ item.title }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data(){
    return{
      items: [
        { title: 'hogehoge' },
        { title: 'ahiahi' }
      ]
    }
  },
  methods:{
    async getLib(){
      const url = "/database";
      const res = await axios.get(url);
      
    }
  }
}
</script>