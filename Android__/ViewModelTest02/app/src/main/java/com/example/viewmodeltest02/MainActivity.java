package com.example.viewmodeltest02;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProvider;
import androidx.lifecycle.ViewModelProviders;

import android.os.Bundle;
import android.os.PersistableBundle;
import android.view.View;

import com.example.viewmodeltest02.databinding.ActivityMainBinding;

public class MainActivity extends AppCompatActivity {
    final static String KEY_NUMBER = "my_number";
    ActivityMainBinding binding;
    myViewModel myviewmodel;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = DataBindingUtil.setContentView(this,R.layout.activity_main);
        this.myviewmodel = ViewModelProviders.of(this).get(myViewModel.class);
    }


}
