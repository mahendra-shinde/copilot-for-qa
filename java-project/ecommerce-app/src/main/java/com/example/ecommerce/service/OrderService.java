package com.example.ecommerce.service;

import com.example.ecommerce.entity.OrderEntity;
import com.example.ecommerce.repository.OrderRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class OrderService {

    private final OrderRepository orderRepository;

    public OrderEntity createOrder(OrderEntity order) {
        order.setStatus("CREATED");
        return orderRepository.save(order);
    }

    public List<OrderEntity> getOrders(Long userId) {
        return orderRepository.findByUserId(userId);
    }
}
