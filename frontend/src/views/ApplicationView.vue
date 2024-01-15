<template>
  <div>
    <v-container>
      <v-form>
        <h3>Apply for vacancy</h3>
        <v-text-field label="First name" v-model="first_name"></v-text-field>
        <v-text-field label="Last name" v-model="last_name" ></v-text-field>
        <v-text-field label="E-mail" v-model="email" ></v-text-field>
        <v-radio-group v-model="gender" label="Gender" >
          <v-radio label="Male" value="male"></v-radio>
          <v-radio label="Female" value="female"></v-radio>
        </v-radio-group>
        <v-menu>
          <v-text-field slot="activator" :value="date_of_birth" label="Date of birth" v-model="date_of_birth" ></v-text-field>
          <v-date-picker v-model="date_of_birth"></v-date-picker>
        </v-menu>
      </v-form>
    </v-container>
  </div>
</template>

<script>
export default {
    data(){
      return{
        first_name: '',
        last_name: '',
        gender: '',
        email: '',
        date_of_birth : null,
        phone_number: '',
        address: '',
        current_class: '',
        school: '',
        school_location: '',
        school_phone_number: '',
        change_reason: '',
        class_applied_for: '',
        recommendation_letter: null,
        passport: null,
        results_document: null,
        guardian_name: '',
        guardian_phone_number: '',
        guardian_email: '',
        relationship_with_guardian: '',
        religion: '',
        combination_applied_for: '',
        disabled: false,
        disabled_description: '',
        any_chronic_disease_condition: false,
        chronic_disease_condition_description: false

      }
    }
}
</script>

<style scoped>

</style>