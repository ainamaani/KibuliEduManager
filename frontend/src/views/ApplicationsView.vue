<template>
  <div class="applications">
    <h3>Applications list</h3>

    <v-data-table :headers="headers" :items="applications" item-key="id">
      <template v-slot:items="props">
        <td>{{ props.item.first_name }}</td>
        <td>{{ props.item.last_name }}</td>
        <td>{{ props.item.gender }}</td>
        <td>{{ props.item.phone_number }}</td>
        
      </template>
    </v-data-table>
  </div>
</template>

<script>

export default {
  data(){
    return{
      applications: [],
      headers: [
        { text: 'First Name', value: 'first_name' },
        { text: 'Last Name', value: 'last_name' },
        { text: 'Gender', value: 'gender' },
        { text: 'Phone number', value: 'phone_number' },
        { text: 'Actions', value: 'actions', sortable: false },
      ]
    }
  },
  methods: {
    getAllApplications(){
      fetch('http://localhost:8000/api/applications/',{
        method: 'GET'
      })
      .then(response => response.json())
      .then((data)=>{
        console.log(data)
        this.applications = data;
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  },
  mounted(){
      this.getAllApplications()
  }
}
</script>

<style scoped>

</style>