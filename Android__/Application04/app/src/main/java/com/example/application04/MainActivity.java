package com.example.application04;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.ViewModelProvider;
import androidx.lifecycle.ViewModelProviders;

import android.os.Bundle;
import android.os.PersistableBundle;

import com.example.application04.databinding.ActivityMainBinding;

public class MainActivity extends AppCompatActivity {
    ActivityMainBinding binding;
    ViewModelTest myviewtest;
    public final static String KEY_NUMBER = "my_number";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //setContentView(R.layout.activity_main);
        binding = DataBindingUtil.setContentView(this,R.layout.activity_main);
        myviewtest = ViewModelProviders.of(this,new SavedStateVMFactory(this)).get(ViewModelTest.class);

        binding.setData(myviewtest);
        binding.setLifecycleOwner(this);
    }

}
