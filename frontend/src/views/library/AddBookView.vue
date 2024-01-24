<template>
  <div class="add-book">
    <v-container>
        <v-form @submit.prevent="handleAddBookSubmission">
            <h3>Add book</h3>
            <v-text-field label="Book title" v-model="title" ></v-text-field>
            <v-text-field label="ISBN" v-model="isbn" ></v-text-field>
            <v-text-field label="Book author" v-model="author" ></v-text-field>
            <v-textarea label="Book description" v-model="description" ></v-textarea>
            <v-text-field type="number" label="Edition" v-model="edition" ></v-text-field>
            <v-text-field label="Book publisher" v-model="publisher" ></v-text-field>
            <v-text-field type="date" label="Publication date" v-model="publication_date" ></v-text-field>
            <v-text-field type="number" label="Number of pages" v-model="number_of_pages" ></v-text-field>
            <v-text-field label="Category" v-model="category" ></v-text-field>
            <v-text-field label="Language" v-model="language" ></v-text-field>
            <v-text-field type="number" label="Number of copies" v-model="number_of_copies" ></v-text-field>

            <v-btn variant="elevated" color="primary" type="submit" >Add book</v-btn>
        </v-form>
    </v-container>
  </div>
</template>

<script>
export default {
    data(){
        return{
            title: '',
            isbn: '',
            author: '',
            publisher: '',
            number_of_pages: 0,
            description: '',
            publication_date: null,
            category: '',
            language: '',
            edition: 0,
            number_of_copies: 0,
        }
    },
    methods: {
        handleAddBookSubmission(){
            const bookData = {
                title:this.title, isbn:this.isbn, author:this.author, publisher:this.publisher,
                number_of_pages:this.number_of_pages, description:this.description,
                publication_date:this.publication_date, category:this.category,
                language:this.language, edition:this.edition,number_of_copies:this.number_of_copies
            }
            fetch('http://localhost:8000/api/library/addbook',{
                method: 'POST',
                headers:{
                    'Content-Type':'application/json'
                },
                body: JSON.stringify(bookData)
            })
            .then((response)=>{
                if(response.status === 201){
                    console.log('Book addition successful');

                    this.title = '', 
                    this.isbn = '', 
                    this.author = '', 
                    this.publisher = '',
                    this.number_of_pages = 0, 
                    this.description = '',
                    this.publication_date = null, 
                    this.category = '',
                    this.language = '', 
                    this.edition = 0,
                    this.number_of_copies = 0

                }
            })
            .catch((err)=>{
                console.log(err)
            })
        }
    }
}
</script>

<style scoped>

</style>