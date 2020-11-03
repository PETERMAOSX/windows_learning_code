package com.example.baskballdemo;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProviders;
import android.os.Bundle;
import android.os.PersistableBundle;
import android.view.View;

import com.example.baskballdemo.databinding.ActivityMainBinding;

public class MainActivity extends AppCompatActivity {
    ActivityMainBinding binding;
    ViewModelTest viewModelTest;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //setContentView(R.layout.activity_main);
//        if(savedInstanceState!=null){
//
//        }
        binding = DataBindingUtil.setContentView(this,R.layout.activity_main);
        viewModelTest = ViewModelProviders.of(this).get(ViewModelTest.class);
        viewModelTest.getA_teamValue().observe(this, new Observer<Integer>() {
            @Override
            public void onChanged(Integer integer) {
                binding.textA.setText(String.valueOf(integer));
            }
        });
        viewModelTest.getB_teamValue().observe(this, new Observer<Integer>() {
            @Override
            public void onChanged(Integer integer) {
                binding.textB.setText(String.valueOf(integer));
            }
        });
        binding.A1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                viewModelTest.A_add(1);
            }
        });
        binding.A2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                viewModelTest.A_add(2);
            }
        });
        binding.B1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                viewModelTest.B_add(1);
            }
        });
        binding.B2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                viewModelTest.B_add(2);
            }
        });
        binding.Reset.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                viewModelTest.reset();
            }
        });
        binding.Back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                viewModelTest.undo();
            }
        });
        binding.button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                viewModelTest.A_add(3);
            }
        });
        binding.button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                viewModelTest.B_add(3);
            }
        });
    }

//    @Override
//    public void onSaveInstanceState(@NonNull Bundle outState, @NonNull PersistableBundle outPersistentState) {
//        super.onSaveInstanceState(outState, outPersistentState);
//        outState.putInt();
//    }
}
